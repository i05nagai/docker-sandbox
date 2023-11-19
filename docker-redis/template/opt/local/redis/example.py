import redis


def main():
    host = "172.18.0.2"
    host = "127.0.0.1"
    r = redis.Redis(
        host=host,
        port=6379,
    )

    r.set('foo', 'bar')
    value = r.get('foo')
    print(value)

    # Convert to a bytes, string, int or float first.
    complex_data = {
        "1": [1, 2, 3, 4],
        "2": None,
        "3": {
            "11": 1.1
        }
    }
    r.hmset('foo2', complex_data)
    value = r.get('foo2')
    print(value)


if __name__ == '__main__':
    main()
