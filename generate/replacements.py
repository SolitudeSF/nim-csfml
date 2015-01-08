# Copyright (C) 2015 Oleh Prypin <blaxpirit@gmail.com>
#
# This file is part of nim-csfml.
#
# This software is provided 'as-is', without any express or implied
# warranty. In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgement in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.


import sys
import re

(fn,) = sys.argv[1:]

with open(fn) as f:
    s = f.read()

# MouseButton.ButtonCount -> MouseButton.Count
s = s.replace('sfMouseButtonCount', 'sfMouseCount')

# (anonymous struct) -> WindowStyle
# https://github.com/LaurentGomila/CSFML/commit/ed44d9e0db2e65f49ce6eb2f1dc0de755066e24b
s = re.sub(
    r'(enum\s*?\{\s*?sfNone([^\{]|\n)+?sfDefaultStyle.+?\})',
    r'typedef \1 sfWindowStyle', s, flags=re.S
)

# WindowStyle.DefaultStyle -> WindowStyle.Default
s = s.replace('sfDefaultStyle', 'sfDefault')

with open(fn, 'w') as f:
    f.write(s)