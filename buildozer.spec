[app]

title = ASHU APP
package.name = basicapp
package.domain = net.aesencryptornl
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*.jpg
requirements = python3,kivy
version = 0.1
orientation = portrait

[buildozer]

log_level = 2
warn_on_root = 1

[buildozer.android]

fullscreen = 0
android.minapi = 21
android.api = 33
android.ndk = 19b
android.sdk = 24
android.permissions = INTERNET
android.arch = arm64-v8a, armeabi-v7a
android.gradle_dependencies = androidx.core:core:1.10.1
android.fileprovider = True
android.entrypoint = org.kivy.android.PythonActivity
android.manifest.theme = @android:style/Theme.NoTitleBar
android.update_sdk = True
android.javac_target = 1.8
