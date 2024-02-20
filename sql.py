from sender import sendToPartner


def insert(data):
    first, last, email, bio, password, role = data

    query = f"INSERT INTO `accounts` (`first_name`, `last_name`, `email`,`bio`, `password_hash`, `role`) VALUES ({first}, {last}, {email}, {bio}, {password}, {role})"
    sendToPartner(query)
