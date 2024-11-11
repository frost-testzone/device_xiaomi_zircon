#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'system_ext/priv-app/ImsService/ImsService.apk': blob_fixup()
        .apktool_patch('ImsService-patches/'),
    'system_ext/lib64/libsink.so': blob_fixup()
        .add_needed('libshim_sink.so'),
    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libui_shim.so'),
    'odm/lib64/hw/vendor.xiaomi.sensor.citsensorservice@2.0-impl.so': blob_fixup()
        .add_needed('libui_shim.so'),
    'vendor/bin/hw/android.hardware.security.keymint@2.0-service.mitee': blob_fixup()
        .add_needed('android.hardware.security.rkp-V3-ndk.so'),
    'vendor/etc/init/vendor.xiaomi.hardware.vibratorfeature.service.rc': blob_fixup()
        .regex_replace('/odm/bin', '/vendor/bin'),
}  # fmt: skip

module = ExtractUtilsModule(
    'zircon',
    'xiaomi',
    blob_fixups=blob_fixups,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
