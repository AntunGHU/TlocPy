# Thanks to Zachary for originally posting this on the discussion board!
# 
# 
# Rather than typing the long/ugly command to create a new file using powershell, you can set up a # custom function to mimic the touch command you'll see me use on my mac.
# 
# 
# Creating a temporary function
# 
# If you were to run the following in your terminal:
# 
# 
# function touch {New-Item -ItemType File -Name ($args[0])}
# 
#  it will create a temporary function (temp meaning while that instance of PowerShell is open) # that will allow you to type:
# 
# 
# touch filename
# 
# 
# 
# 
# Creating a "permanent" function
# 
# 
# 
# 
# To make this a "permanent" change it just needs to be added to the PowerShell profile found at:
# 
# 
# C:\Users\USERSNAMEHERE\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
# 
# Note that you need to alter the above path to reflect your actual username.
# 
# 
# First run:
# 
# 
# Test-Path $PROFILE
# 
# to check if a profile file already exist.
# 
# 
# If True , then navigate to the above location and copy and paste in the function line. Restart # PowerShell.
# 
# 
# If False , then enter the below command to create a new empty profile: (ONLY DO IF NO PROFILE IS # FOUND AS THE -force FLAG WILL OVERWRITE ANY EXISTING PROFILE)
# 
# 
# New-Item -Path $PROFILE -Type File -force
# 
# 
# 
# 
# At this point navigate to the above profile location and paste in the function. Restart # PowerShell. You can now type touch to create new empty files encoded with UTF-8.