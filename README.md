How It Works:
Admin Paths: The script uses a list of common admin panel paths (e.g., admin, login, wp-admin, etc.).
URL Construction: It appends each path to the target website URL and sends an HTTP GET request.
Response Check: If the response status code is 200, it means the path exists, and the script prints the URL.
Error Handling: The script handles exceptions like connection errors or timeouts.

Example Usage:
Save the script as admin_panel_finder.py.

Run the script:
python admin_panel_finder.py

Enter the target website URL when prompted:
Enter the target website URL (e.g., http://example.com): http://example.com

Output Example:
Scanning http://example.com/ for admin panels...

[+] Found: http://example.com/admin (Status: 200)
[-] Not found: http://example.com/login (Status: 404)
[-] Not found: http://example.com/wp-admin (Status: 404)


Notes:
Ethical Use: Only use this script on websites you own or have explicit permission to test. Unauthorized scanning is illegal and unethical.
Customization: You can add more paths to the admin_paths list or modify the script to suit your needs.
Performance: For large websites, consider adding threading or asynchronous requests to speed up the process.
