# CommerceHub
A simple e-commerce web application

## User stories

### Users

- A user should be able to register an account on our site using his/her email address and a password.

- A user can do 3 things on the site: browse available items, buy an item, or sell an item. A user has a view of all pending/completed buy requests and sell requests he made, and modify their status.

- To buy/sell an item, the user will be required to login. To view available items, a user is not required to login.

- To buy an item, user need to provide his/her credit card number. For simplicity, we’ll implement a credit card validator.

- To sell an item, user need to:

    - Take 3 pictures of the item from 3 different angles, provide user’s address.

    - Once the administrator approve the pictures, user’s item can be viewed among the available listings.

    - If the item is bought, user will be notified via email and will be given 3 time slots on the next day during which time he/she wants our staff to collect and deliver the item.

### Staff

- A staff should have either one of the following roles: Administrator or Collector.

- An Administrator is not allowed to buy or sell items. An Administrator can view all unapproved sell request and give them comments/approve them.

- A Collector could modify the status of buy requests/sell requests assigned to him.

### States of objects

- A (Sell)Request on our site has the following states: PENDING_APPROVAL or APPROVED.

- An Item on our site has the following states: LISTED, BOUGHT, IN_DELIVERY, TRANSACTED

## Architecture

Reference: [This wonderful Flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

`/commerce_hub.py`: Python script that runs the application.

`/app`: The Python package that hosts the applicaiton. In Python, a sub-directory that includes a `__init__.py` file is considered a package, and can be imported. When you import a package, the `__init__.py` executes and defines what symbols the package exposes to the outside world.

### Routes

Splitting routes by access right:

    1. Everyone could access: `/home`, `/register`, `/login`

    2. Only logged in users: `/buy/{item-id}`, `/sell/new/`, `/monitor/view`, `/monitor/edit`

    3. Only Administrator: `/admin/requests`

    4. Only Collector: `/collect/assigned` and `/collect/completed`

