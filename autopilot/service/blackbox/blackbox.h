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
  
 Blackbox Publisher Interface

 Copyright (C) 2014 Tobias Simon, Ilmenau University of Technology

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. */



#ifndef __BLACKBOX_H__
#define __BLACKBOX_H__


#include "../platform/platform.h"
#include "../util/math/vec2.h"


#define BLACKBOX_ITEMS 35


extern char *blackbox_spec[BLACKBOX_ITEMS];


/* initialize blackbox */
void blackbox_init(void);


/* publish a blackbox record */
void blackbox_record(const float dt, /* sensor inputs ... */
               const marg_data_t *marg_data,
               const gps_data_t *gps_data,
               const float ultra,
               const float baro,
               const float voltage,
               const float current,
               const float channels[MAX_CHANNELS],
               const uint16_t sensor_status,
               const vec2_t *ne_pos_err, /* NEU position errors ... */
               const float u_pos_err,
               const vec2_t *ne_spd_err, /* NEU speed errors ... */
               const float u_spd_err,
               const vec3_t *mag_normal);


#endif /* __BLACKBOX_H__ */

