/*___________________________________________________
 |  _____                       _____ _ _       _    |
 | |  __ \                     |  __ (_) |     | |   |
 | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
 | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
 | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
 | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
 |                   __/ |                           |
 |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
 |___________________________________________________|
  
 Replay Main Implementation

 Copyright (C) 2014 Tobias Simon, Ilmenau University of Technology

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. */


#include <util.h>
#include <assert.h>
#include <fcntl.h>
#include <unistd.h>
#include <msgpack.h>
#include <sys/stat.h>
#include "main_loop.h"
#include "../blackbox/blackbox.h"


#define INPUT_VARIABLES (sizeof(blackbox_spec) / sizeof(char *))


static int get_index(char *name)
{
   FOR_N(i, INPUT_VARIABLES)
   {
      if (strcmp(name, blackbox_spec[i]) == 0)
      {
         return i;
      }
   }
   return -1;
}


static int index_table[1024];
static float double_data[INPUT_VARIABLES];
static int int_data[INPUT_VARIABLES];


void handle_array(msgpack_object array, int header)
{
   int index = 0;
   msgpack_object *p = array.via.array.ptr;
   msgpack_object *const pend = array.via.array.ptr + array.via.array.size;
   for (; p < pend; ++p)
   {
      if (header)
      {
         char name[1024];
         memcpy(name, p->via.raw.ptr, p->via.raw.size);
         name[p->via.raw.size] = '\0';
         int idx = get_index(name);
         assert(idx != -1);
         index_table[index] = idx;
      }
      else
      {
         int idx = index_table[index];
         if (idx >= 0)
         {
            switch (p->type)
            {
               case MSGPACK_OBJECT_DOUBLE:
                  double_data[idx] = p->via.dec;
                  break;
            
               case MSGPACK_OBJECT_POSITIVE_INTEGER:
                  int_data[idx] = p->via.i64;
                  break;
            
               case MSGPACK_OBJECT_NEGATIVE_INTEGER:
                  int_data[idx] = p->via.u64;
                  break;

               default:
                  break;
            }
         }
      }
      index++;
   }
}


/* a replay of previously recorded flight data */
void main_replay(int argc, char *argv[])
{
   assert(argc > 1);
   main_init(argc, argv);
   int file = open(argv[1], O_RDONLY);
   if (file < 0)
   {
      printf("could not open file: %s\n", argv[1]);
      return;
   }
   
   struct stat st;
   stat(argv[1], &st);
   size_t size = st.st_size;

   char *buffer = malloc(size);
   if (read(file, buffer, size) < 0)
   {
      printf("could not read from file: %s\n", argv[1]);
   }

   msgpack_unpacked msg;
   msgpack_unpacked_init(&msg);
                
   size_t off = 0;
   DATA_DEFINITION();
   msgpack_unpack_next(&msg, buffer, size, &off);
   handle_array(msg.data, 1);
   while (msgpack_unpack_next(&msg, buffer, size, &off))
   {
      handle_array(msg.data, 0);
      dt = double_data[0];
      FOR_N(i, 3)
      {
         marg_data.gyro.ve[i] = double_data[1 + i];
      }
      FOR_N(i, 3)
      {
         marg_data.acc.ve[i] = double_data[4 + i];
      }
      FOR_N(i, 3)
      {
         marg_data.mag.ve[i] = double_data[7 + i];
      }
      gps_data.lat = double_data[10];
      gps_data.lon = double_data[11];
      gps_data.alt = double_data[12];
      gps_data.course = double_data[13];
      gps_data.speed = double_data[14];
      ultra_z = double_data[15];
      baro_z = double_data[16];
      voltage = double_data[17];
      current = double_data[18];
      FOR_N(i, MAX_CHANNELS)
      {
         channels[i] = double_data[19 + i];
      }
      sensor_status = int_data[25];
      main_step(dt, &marg_data, &gps_data, ultra_z, baro_z, voltage, current, channels, sensor_status, 1);
   }
   free(buffer);
   msgpack_unpacked_destroy(&msg);
   close(file);
   sleep(1);
}

