[![Build Status](https://travis-ci.com/dabapps/test-project.svg?token=apzD3FKHpTNKHAtAu9xC&branch=master)](https://travis-ci.com/dabapps/test-project)

# test_project

## Dev Setup

### Local

#### Creating the database

```bash
$ psql -d postgres
$ create database test_project;
```

#### Building the project

```bash
$ ctf project run build
```

#### Tests

```bash
$ ctf project run runtests
```

#### Routing

```bash
$ ctf router test-project.ctf.sh --ident test-project:development:web
```
