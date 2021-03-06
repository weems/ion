#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
{
  'includes' : [
    '../common.gypi',
  ],

  'target_defaults': {
    'includes' : [
      '../dev/target_visibility.gypi',
    ],
  },

  'targets' : [
    {
      'target_name' : 'statetable',
      'type': 'static_library',
      'sources' : [
        'statetable.cc',
        'statetable.h',
      ],
      'conditions': [
        ['OS == "windows"', {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=APIENTRY',
            ],  # defines
          },
        }, {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=',
            ],
          },
        }],
      ],
      'dependencies': [
        '../portgfx/portgfx.gyp:ionportgfx',
        '<(ion_dir)/math/math.gyp:ionmath',
      ],
    },  # target: statetable

    {
      'target_name' : 'tracinghelper',
      'type': 'static_library',
      'sources' : [
        'tracinghelper.cc',
        'tracinghelper.h',
      ],
      'conditions': [
        ['OS == "windows"', {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=APIENTRY',
            ],  # defines
          },
        }, {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=',
            ],
          },
        }],
      ],
      'dependencies': [
        '../portgfx/portgfx.gyp:ionportgfx',
      ],
    },  # target: tracinghelper

    {
      'target_name' : 'graphicsmanager',
      'type': 'static_library',
      'sources' : [
        'glfunctions.inc',
        'graphicsmanager.cc',
        'graphicsmanager.h',
        'graphicsmanagermacrodefs.h',
        'graphicsmanagermacroundefs.h',
      ],
      'conditions': [
        ['OS == "windows"', {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=APIENTRY',
            ],  # defines
          },
        }, {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=',
            ],
          },
        }],
      ],
      'cflags_cc': [
        '-Wno-unused-local-typedef',
      ],
      'all_dependent_settings': {
        'cflags_cc': [
          '-Wno-unused-local-typedef',
        ],
      },
      'dependencies': [
        ':statetable',
        ':tracinghelper',
        '../portgfx/portgfx.gyp:ionportgfx',
        '<(ion_dir)/math/math.gyp:ionmath',
      ],
    },  # target: graphicsmanager

    {
      'target_name' : 'iongfx',
      'type': 'static_library',
      'sources' : [
        'attribute.cc',
        'attribute.h',
        'attributearray.cc',
        'attributearray.h',
        'bufferobject.cc',
        'bufferobject.h',
        'cubemaptexture.cc',
        'cubemaptexture.h',
        'framebufferobject.cc',
        'framebufferobject.h',
        'image.cc',
        'image.h',
        'indexbuffer.cc',
        'indexbuffer.h',
        'iresource.h',
        'node.cc',
        'node.h',
        'openglobjects.h',
        'renderer.cc',
        'renderer.h',
        'resourceholder.cc',
        'resourceholder.h',
        'resourcemanager.cc',
        'resourcemanager.h',
        'sampler.cc',
        'sampler.h',
        'shader.cc',
        'shader.h',
        'shaderinput.cc',
        'shaderinput.h',
        'shaderinputregistry.cc',
        'shaderinputregistry.h',
        'shaderprogram.cc',
        'shaderprogram.h',
        'shape.cc',
        'shape.h',
        'texture.cc',
        'texture.h',
        'texturemanager.cc',
        'texturemanager.h',
        'tracecallextractor.cc',
        'tracecallextractor.h',
        'uniform.cc',
        'uniform.h',
        'uniformblock.cc',
        'uniformblock.h',
        'uniformholder.cc',
        'uniformholder.h',
        'updatestatetable.cc',
        'updatestatetable.h',
      ],
      'conditions': [
        # Thanks to graphicsmanagermacrodefs.h's usage of ION_APIENTRY, in
        # practice most dependents of this library will need ION_APIENTRY defined.
        ['OS == "windows"', {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=APIENTRY',
            ],  # defines
          },
        }, {
          'all_dependent_settings': {
            'defines': [
              'ION_APIENTRY=',
            ],
          },
        }],
      ],
      'dependencies': [
        ':graphicsmanager',
        ':statetable',
        ':tracinghelper',
        '../portgfx/portgfx.gyp:ionportgfx',
        '<(ion_dir)/base/base.gyp:ionbase',
        '<(ion_dir)/math/math.gyp:ionmath',
        '<(ion_dir)/port/port.gyp:ionport',
      ],
    },  # target: iongfx

    {
      'target_name': 'iongfx_for_tests',
      'type': 'static_library',
      'sources': [
        'tests/mockgraphicsmanager.cc',
        'tests/mockgraphicsmanager.h',
        'tests/mockvisual.cc',
        'tests/mockvisual.h',
        'tests/testscene.cc',
        'tests/testscene.h',
        'tests/traceverifier.cc',
        'tests/traceverifier.h',
      ],
      'dependencies': [
        ':iongfx',
        '../portgfx/portgfx.gyp:ionportgfx_for_tests',
        # traceverifier.cc uses gtest.h, so we need the proper #defines and
        # include paths:
        '<(ion_dir)/external/gtest.gyp:iongtest_safeallocs_no_main',
        '<(ion_dir)/base/base.gyp:ionbase_for_tests',
        '<(ion_dir)/math/math.gyp:ionmath_for_tests',
      ],
    },  # target: iongfx_for_tests
  ],
}
