[app]

title = Ashwatt App
package.name = basicapp
package.domain = net.aesencryptornl
source.dir = .
source.include_exts = py,png,jpg,txt,kv,atlas,json
source.include_patterns = assets/*.jpg
requirements = python3,kivy,android,pyjnius
version = 0.1
orientation = portrait

[buildozer]

log_level = 2
warn_on_root = 1

[buildozer.android]

fullscreen = 0
android.api = 34
android.minapi = 21
android.ndk = 19b
android.sdk = 24
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.arch = arm64-v8a, armeabi-v7a
android.entrypoint = org.kivy.android.PythonActivity
android.manifest.theme = @android:style/Theme.NoTitleBar
android.update_sdk = True
android.javac_target = 1.8
