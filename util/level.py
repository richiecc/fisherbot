"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from re import L
from util.level_table import level_dict


# A q p
#    W
def levelFromXP(xp:int):
    previous_index = None
    for xp_barrier in level_dict.keys():
        if xp_barrier < xp:
            previous_index = xp_barrier
            continue
        elif xp_barrier == xp:
            return level_dict[xp_barrier]
        elif xp_barrier > xp:
            break
        elif xp > 200000000:
            return level_dict[200000000]
        else:
            return "LEVEL BROKE???"
    return level_dict[previous_index]
