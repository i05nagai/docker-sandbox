# This file is used by Rack-based servers to start the application.

require_relative "config/environment"

# Rails.application.routes.draw do
#   # root "articles#index"
# 
#   # get "/articles", to: "articles#index"
#   # get "/articles/:id", to: "articles#show"
#   resources :articles do
#     resources :comments
#   end
# end

run Rails.application
Rails.application.load_server

