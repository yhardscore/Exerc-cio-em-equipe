$exclude = @("venv", "botWeb.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botWeb.zip" -Force