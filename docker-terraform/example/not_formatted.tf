resource "google_sql_database_instance" "db" {
  name = "db"
  database_version= "MYSQL_5_7"
  region = "asia-northeast1"
  master_instance_name = "${self.name}-master"

  settings {
    tier = "db-g1-small"

    bacup_configuration {
      binary_log_enabled = true
      enabled = true

      # UTC
      start_time = "12:00"
    }

    ip_configuration {
      ipv4_enabled = true
    }
  }
}

resource "google_sql_database" "users" {
  name = "users-db"
  instance = "${google_sql_database_instance.master.name}"
  charset = "latin1"
  collation = "latin1_swedish_ci"
}

resource "google_sql_user" "users" {
  name = "me"
  instance = "${google_sql_database_instance.master.name}"
  host = "me.com"
  password = "changeme"
}
