[app]
title = ashwatt
package.name = ashuapp
package.domain = com.yourdomain
source.include_exts = py,png,jpg,kv
source.include_patterns = assets/*.jpg
source.exclude_exts = spec
version = 1.0
requirements = python3,kivy,kivymd,,urllib3
android.permissions = INTERNET
android.api = 33  # Android 15
android.minapi = 21
android.ndk = 25b
android.foreground = True

# ✅ Enable faster builds
p4a.android_dir = $HOME/.buildozer/android/platform/python-for-android
android.accept_sdk_license = True
