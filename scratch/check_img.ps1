Add-Type -AssemblyName System.Drawing
$imgPath = "D:\Irtaza Proj\Swiftcare Solutions Full Stack Website\images\logooo.png"
$img = [System.Drawing.Image]::FromFile($imgPath)
Write-Host "$($img.Width)x$($img.Height)"
$img.Dispose()
