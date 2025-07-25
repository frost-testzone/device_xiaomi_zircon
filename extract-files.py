#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/zircon',
    'hardware/mediatek',
    'hardware/xiaomi'
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libarcsoft_beautyshot',
        'libmialgo_utils',
        'libmpbase'
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    ('odm/lib64/nfc_nci.nqx.default.hw.so', 'odm/lib64/nfc_nci.thn31nfc.tms.so', 'odm/lib64/tms-utils.so', 'vendor/lib64/libnvram.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'odm/lib64/hw/vendor.xiaomi.sensor.citsensorservice@2.0-impl.so': blob_fixup()
        .add_needed('libui_shim.so'),
    'vendor/bin/hw/android.hardware.graphics.composer@3.1-service': blob_fixup()
        .replace_needed('android.hardware.graphics.composer@2.1-resources.so', 'android.hardware.graphics.composer@2.1-resources-v34.so'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    'vendor/bin/hw/android.hardware.security.keymint@2.0-service.mitee': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V2-ndk.so', 'android.hardware.security.keymint-V3-ndk.so')
        .add_needed('android.hardware.security.rkp-V3-ndk.so'),
    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v32.so'),
    'vendor/etc/init/vendor.xiaomi.hardware.vibratorfeature.service.rc': blob_fixup()
        .regex_replace('/odm/bin', '/vendor/bin'),
    ('vendor/lib64/hw/hwcomposer.mtk_common.so', 'vendor/lib64/libmialgoengine.so', 'vendor/lib64/mt6886/libcam.hal3a.ctrl.so', 'vendor/lib64/mt6886/libcam.hal3a.so', 'vendor/lib64/mt6886/libmtkcam_cputrack.so', 'vendor/lib64/mt6886/libmtkcam_request_requlator.so'): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    ('vendor/lib64/libalLDC.so', 'vendor/lib64/libalAILDC.so', 'vendor/lib64/libalhLDC.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/mt6886/libneuralnetworks_sl_driver_mtk_prebuilt.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    ('vendor/lib64/libcodec2_vpp_AIMEMC_plugin.so', 'vendor/lib64/libcodec2_vpp_AISR_plugin.so'): blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so')
        .replace_needed('android.hardware.graphics.common-V3-ndk.so', 'android.hardware.graphics.common-V6-ndk.so'),
    ('vendor/lib/vendor.mediatek.hardware.pq_aidl-V1-ndk.so', 'vendor/lib/vendor.mediatek.hardware.pq_aidl-V2-ndk.so', 'vendor/lib/vendor.mediatek.hardware.pq_aidl-V3-ndk.so',
    'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V1-ndk.so', 'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V2-ndk.so', 'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V3-ndk.so'): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V3-ndk.so', 'android.hardware.graphics.common-V6-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'zircon',
    'xiaomi',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
    lib_fixups=lib_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
