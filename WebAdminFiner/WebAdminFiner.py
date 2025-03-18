import requests

def find_admin_panel(url):
    # List of common admin panel paths
    admin_paths = [
        "admin", "login", "wp-admin", "admin/login", "adminpanel",
        "administrator", "backend", "cp", "controlpanel", "dashboard",
        "manager", "management", "admincp", "admin_area", "admin-login",
        "admin_login", "admin123", "adminarea", "admincontrol", "adminpanel",
        "adminportal", "adminweb", "moderator", "user", "admin1", "admin2",
        "admin3", "admin4", "admin5", "sysadmin", "system-administrator",
        "root", "superuser", "superadmin", "webadmin", "operator", "panel",
        "cpanel", "cpaneladmin", "cpaneluser", "phpmyadmin", "myadmin",
        "mysql", "sqladmin", "sql", "dbadmin", "db", "database"
    ]

    # Ensure the URL ends with a slash
    if not url.endswith("/"):
        url += "/"

    print(f"Scanning {url} for admin panels...\n")

    # Loop through each admin path and check if it exists
    for path in admin_paths:
        full_url = url + path
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found: {full_url} (Status: {response.status_code})")
            else:
                print(f"[-] Not found: {full_url} (Status: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {full_url}: {e}")

if __name__ == "__main__":
    # Input the target website URL
    target_url = input("Enter the target website URL (e.g., http://example.com): ").strip()
    find_admin_panel(target_url)