[app]
title = V2IT Fiber Optic Calculator
package.name = v2itfiberoptic
package.domain = org.v2it
source.dir = .
source.include_exts = py,png,jpg,kv,txt,md
version = 1.0
requirements = python3,kivy
orientation = portrait
icon.filename = logo.png

# Tambahkan jika ingin menyimpan APK di tempat default CI suka cari
android.arch = armeabi-v7a,arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
android.sdk = 24
android.ndk = 19b
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
