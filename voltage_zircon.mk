#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common VoltageOS stuff.
$(call inherit-product, vendor/voltage/config/common_full_phone.mk)

# Inherit from zircon device
$(call inherit-product, device/xiaomi/zircon/device.mk)

# VoltageOS flags.
EXTRA_UDFPS_ANIMATIONS := true
TARGET_FACE_UNLOCK_SUPPORTED := true
TORCH_STR_SUPPORTED := true
PERF_ANIM_OVERRIDE := true

# VoltageOS CPUsets configuration.
VOLTAGE_CPU_SMALL_CORES := 0,1,2,3,4,5
VOLTAGE_CPU_BIG_CORES := 6,7
VOLTAGE_ALL_CORES := 0-7
VOLTAGE_CPU_SYS_BG := 0-3
VOLTAGE_CPU_BG := 0-2
VOLTAGE_CPU_FG := 0-7
VOLTAGE_CPU_LIMIT_BG := 0-2
VOLTAGE_CPU_LIMIT_UI := 0-5
VOLTAGE_CPU_DISPLAY := 6-7

# Bootanimation Resolution.
TARGET_BOOT_ANIMATION_RES := 1920

PRODUCT_NAME := voltage_zircon
PRODUCT_DEVICE := zircon
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 23090RA98G

PRODUCT_SYSTEM_NAME := zircon_global
PRODUCT_SYSTEM_DEVICE := zircon

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="zircon_global-user 15 AP3A.240905.015 OS2.0.207.0.VNOMIXM release-keys" \
    BuildFingerprint=Redmi/zircon_global/zircon:15/AP3A.240905.015.A2/OS2.0.207.0.VNOMIXM:user/release-keys \
    DeviceName=$(PRODUCT_SYSTEM_DEVICE) \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
