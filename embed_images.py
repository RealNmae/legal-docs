import sys

def embed_images(html_file, launch_icon_file, screenshot_file):
    with open(html_file, 'r') as f:
        html_content = f.read()
    
    with open(launch_icon_file, 'r') as f:
        launch_base64 = f.read().strip()
        
    with open(screenshot_file, 'r') as f:
        screenshot_base64 = f.read().strip()
        
    # Replace launch icon
    html_content = html_content.replace('src="launch_icon.png"', f'src="data:image/png;base64,{launch_base64}"')
    
    # Replace screenshot
    html_content = html_content.replace('src="screenshot.png"', f'src="data:image/png;base64,{screenshot_base64}"')
    
    with open(html_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    embed_images('itero.html', 'launch_icon_base64.txt', 'screenshot_base64.txt')
