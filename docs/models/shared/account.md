# Account


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `account_users`                                            | list[*str*]                                                | :heavy_check_mark:                                         | List of the users in the account                           |
| `created_at`                                               | *str*                                                      | :heavy_check_mark:                                         | Timestamp of the account creation date                     |
| `id`                                                       | *float*                                                    | :heavy_check_mark:                                         | The id of the account                                      |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | The name of the account                                    |
| `owner_id`                                                 | *float*                                                    | :heavy_check_mark:                                         | The id of the account owner                                |
| `personal`                                                 | *bool*                                                     | :heavy_check_mark:                                         | If the account is personal or belonging to another account |
| `updated_at`                                               | *str*                                                      | :heavy_check_mark:                                         | Timestamp of the last account update date                  |