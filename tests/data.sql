
INSERT INTO recipes (title, ingredients, instructions, tags)
VALUES
  ('test title', 'test ingredients' || x'0a' || 'body', 'instructions-test', '2018-01-01 00:00:00');

  INSERT INTO users (username, password, email)
VALUES
  ('test', 'test', 'test'),
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f', 'test3@mail.com'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79', 'test4@gmail.com');
