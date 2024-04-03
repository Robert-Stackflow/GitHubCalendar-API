## Github contributions calendar api

By using this API, you can obtain user contribution data easily

## Deploy

- Click the **Deploy Button** to deploy the repository on vercel.

  [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FRobert-Stackflow%2FGitHubCalendar-API)

- For mainland China users, since you can't access the vercel domain correctly, you need to bind a custom domain to use this API.

## Usage

- After deploying to Vercel, assuming your domain name is `git.calendar.com`, you can get the contributions by visiting the following address

  ```
  git.canlendar.com/api?username
  ```

- You can visit this example url which will return my (Robert-Stackflow) contribution history.

  [https://gitcalendar.api.cloudchewie.com/api?Robert-Stackflow](https://gitcalendar.api.cloudchewie.com/api?Robert-Stackflow)

## CORS

- To prevent abuse, you cannot use the example API on your website, it is only used as an example.

- You can also configure CORS by the `allow_origins.txt`

- By default, `allow_origins.txt` contains the following content

  ```
  localhost
  127.0.0.1
  ```

- You can add your own website via wildcard

  ```
  *.example.com
  blog.example.com
  ```

- If the file `allow_origins.txt` does not exist or the file content is empty, all CORS requests are allowed by default.

## Acknowledgments

- [python_github_calendar_api](https://github.com/Zfour/python_github_calendar_api)
