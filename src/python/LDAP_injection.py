def vulnerable_ldap_query(user_input):
    # Simulate LDAP injection
    base_dn = "dc=example,dc=com"
    search_filter = f"(uid={user_input})"
    print(f"LDAP Query: {search_filter}")

# Example test case
vulnerable_ldap_query("admin)(objectClass=*)")
