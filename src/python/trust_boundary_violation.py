def trust_boundary_violation(user_input):
    # Insecure use of unvalidated input
    trusted_data = f"Trusted data: {user_input}"
    print(trusted_data)

# Example test case
trust_boundary_violation("<script>alert('Attack!')</script>")
