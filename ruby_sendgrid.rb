require "httparty"

url = "https://sendgrid.com/api/mail.send.json"

response = HTTParty.post url, :body => {
  "api_user" => "API_USERNAME",
  "api_key" => "API_KEY",
  "to" => "dskrad@me.com",
  "from" => "codecademy@sendgrid.me",
  "subject" => "Hello world",
  "text" => "Congrats! You've sent your second email with SendGrid."
  }

response.body
