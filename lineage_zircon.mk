#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from zircon device
$(call inherit-product, device/xiaomi/zircon/device.mk)

PRODUCT_NAME := lineage_zircon
PRODUCT_DEVICE := zircon
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 23090RA98G

PRODUCT_SYSTEM_NAME := zircon_global
PRODUCT_SYSTEM_DEVICE := zircon

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="zircon_global-user 14 UP1A.231005.007 V816.0.9.0.UNOMIXM release-keys" \
    BuildFingerprint=Redmi/zircon_global/zircon:14/UP1A.231005.007/V816.0.9.0.UNOMIXM:user/release-keys \
    DeviceName=$(PRODUCT_SYSTEM_DEVICE) \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
