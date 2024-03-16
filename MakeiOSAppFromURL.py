import base64, uuid, random

AppName=input("The App Name: ")
AppURL=input("Web URL: ")
AppIcon=input("App Icon\n(JPG or PNG format, with a minimum resolution of at least 72 DPI, in RGB color space, and cannot contain layers or rounded corners. Default path icon.png)\nImage Path: ")
AppOrganization=input("App Organization(Default as EXAMPLE.COM): ")
if AppIcon=="":
    AppIcon="icon.png"
if AppOrganization=="":
    AppOrganization="EXAMPLE.COM"

PayloadIdentifier=f"APP.EXAMPLE.COM/APPLE/{str(random.randint(100000000,999999999))}"

with open(AppIcon, "rb") as image_file:
    Encoded_AppIcon = base64.b64encode(image_file.read()).decode()

ProfileData=f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>ConsentText</key>
<dict>
<key>default</key>
<string>点击安装并输入密码安装本应用 \nChoose 'Install' and enter passcode if prompted.</string>
</dict>
 <key>PayloadContent</key>
 <array>
   <dict>
     <key>FullScreen</key>
     <true/>
     <key>Icon</key>
     <data>{Encoded_AppIcon}</data>
     <key>IsRemovable</key>
     <true/>
     <key>Label</key>
     <string>{AppName}</string>
     <key>PayloadDescription</key>
     <string>Turn any website into an app on your home screen</string>
     <key>PayloadDisplayName</key>
     <string>Web Clip ({AppName})</string>
     <key>PayloadIdentifier</key>
     <string>{PayloadIdentifier}</string>
     <key>PayloadOrganization</key>
     <string>{AppOrganization}</string>
     <key>PayloadType</key>
     <string>com.apple.webClip.managed</string>
     <key>PayloadUUID</key>
     <string>{str(uuid.uuid4())}</string>
     <key>PayloadVersion</key>
     <integer>1</integer>
     <key>Precomposed</key>
     <false/>
     <key>URL</key>
     <string>{AppURL}</string>
   </dict>
 </array>
 <key>PayloadDescription</key>
 <string>Turn any website into an app on your home screen</string>
 <key>PayloadDisplayName</key>
 <string>{AppName}</string>
 <key>PayloadIdentifier</key>
 <string>{PayloadIdentifier}</string>
 <key>PayloadOrganization</key>
 <string>{AppOrganization}</string>
 <key>PayloadRemovalDisallowed</key>
 <false/>
 <key>PayloadType</key>
 <string>Configuration</string>
 <key>PayloadUUID</key>
 <string>{str(uuid.uuid4())}</string>
 <key>PayloadVersion</key>
 <integer>1</integer>
</dict>
</plist>
'''

with open(f"{AppName}.mobileconfig","w") as f:
    f.write(ProfileData)


#Profile=f"data:application/x-apple-aspen-config;base64,{base64.b64encode(ProfileData.encode()).decode()}"


#print(Profile)