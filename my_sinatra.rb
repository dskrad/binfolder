#!/usr/bin/env ruby
#Copyright DSK 2013

require 'sinatra'

get '/' do
  haml :html
end

post '/submit' do
  haml :submit
end

get '/hello/:name' do
  # matches "GET /hello/foo" and "GET /hello/bar"
  # params[:name] is 'foo' or 'bar'
  "Hello #{params[:name]}!"
end

get "/haml" do
  haml "%p 
  The time is now 
  = Time.now" 
end

__END__

@@ html
%p Welcome! Leave your email address for more info!
%form{:method => "post", :action => "/submit"}
  %input{:type =>'text', :name => 'email'}
  %input{:type =>'submit'}

@@ submit
%p Thank you for your submission!
%p= "We will e-mail #{params['email']} when we are ready to launch."
