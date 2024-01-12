package policy
import future.keywords.in

default allow = false

# Allow Django Admin URLs
allow {
    "admin" in input.path
}

# Allow POST requests to create users for admin role
allow {
    input.method == "POST"
    input.path == ["api", "users"]
    input.is_authenticated
    input.roles == ["admin"]
}

# Allow GET requests to retrieve user information
allow {
    input.method == "GET"
    input.path == ["api", "users"]
    input.is_authenticated
}

# Allow POST requests to obtain Token URLs
allow {
    input.method == "POST"
    input.path == ["api", "token"]
}