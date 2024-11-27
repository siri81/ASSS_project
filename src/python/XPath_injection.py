from lxml import etree

def vulnerable_xpath(user_input):
    # XPATH injection vulnerability
    xml = """
    <users>
        <user id="1">
            <username>admin</username>
            <password>password</password>
        </user>
    </users>
    """
    tree = etree.XML(xml)
    result = tree.xpath(f"//user[username/text()='{user_input}']/password/text()")
    return result

# Example test case
print(vulnerable_xpath("admin' or '1'='1"))
