
```
bundle install
bundle exec rails server -p 3000 -b '0.0.0.0'
```

```
bundle exec rails generate controller Articles index --skip-routes

bundle exec rails generate model Article title:string body:text
bundle exec rails db:migrate
```

```
bundle exec rails console
article = Article.new(title: "Hello Rails2", body: "I am on Rails!2")
article.save
```

```
bundle exec rails routes
```

```
bundle exec rails generate model Comment commenter:string body:text article:references
bundle exec rails generate controller Comments
bundle exec rails console
comment = Comment.new(commenter: "Hello Rails", body: "this is comment", article: 1)
comment.save
Article.joins(:comments)
```


```
bundle exec rails generate maintenance_tasks:install
bundle exec rails generate maintenance_tasks:task task1
```

