# -*- coding: utf-8 -*-
# Copyright (C) {{cookiecutter.year}} by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).
{% if cookiecutter.license == "LGPLv3" %}
# This file is part of {{cookiecutter.project_name}}.

# {{cookiecutter.project_name}} is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# {{cookiecutter.project_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with {{cookiecutter.project_name}}.  If not, see <http://www.gnu.org/licenses/>.
{% elif cookiecutter.license == "MIT" %}
# This module is part of {{cookiecutter.project_name}} and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT
{% endif %}

import logging

__version__ = '{{cookiecutter.project_version}}'


logger = logging.getLogger(__name__)
