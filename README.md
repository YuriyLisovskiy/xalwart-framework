# Xalwart Web Framework
[![c++](https://img.shields.io/badge/c%2B%2B-20-6c85cf)](https://isocpp.org/)
[![alpine](https://img.shields.io/badge/Alpine_Linux-0D597F?style=flat&logo=alpine-linux&logoColor=white)](https://alpinelinux.org/)
[![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![macOS](https://img.shields.io/badge/macOS-343D46?style=flat&logo=apple&logoColor=F0F0F0)](https://www.apple.com/macos)

## Contents
* [About](#about)
* [Components](#components)
* [Tools](#tools)
* [Examples](#examples)
* [License](#license)

## About
Xalwart is a C++ web framework for building dynamic applications. The main
purpose of using Xalwart is to build an [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
protocol-based web API.

> In the future, template-based responses will be added, probably.

The framework provides modules, middleware, controllers, global application state
(settings), database access and schema migrations, and commands.

* Module is a logic component of the project. Each module contains commands and
regular expression-based [URL](https://en.wikipedia.org/wiki/URL) patterns mapped
to controllers.

* Middleware can be implemented as classes or functions, so they are called class-based
and function-based respectfully.

* Controllers are handlers of the actual requests. They accept the request and additional
URL parameters in arguments of the appropriate method and return the response object which
can be serialized to HTTP format.

* Application settings define constant parameters which can be set before running the server
directly in the code, or dynamically from the [YAML](https://yaml.org/) configuration file
without recompiling the application. Main YAML config can be overwritten by local, development,
production, etc. files.

* For database access, you can use the [ORM](http://hibernate.org/orm/what-is-an-orm/) component
of this framework. Xalwart ORM provides access to relational databases by using classes mapped
to database entities.

* External management is performed with a set of predefined commands which can be extended by
the developer.

The main purpose of this repository is to provide [docker](https://www.docker.com/) images with
framework components assembled as one package. In the future here will appear prebuilt releases
of the Xalwart framework which can be downloaded for development.

> Full documentation will appear soon in the repositories of every single framework component
> and (or) in this repository as one big wiki. For reference, read [examples](#examples).

## Components
The framework consists of four mandatory parts and one optional.

* ### [xalwart.base](https://github.com/YuriyLisovskiy/xalwart.base)
  Contains common utilities for all other components of the framework.

* ### [xalwart.crypto](https://github.com/YuriyLisovskiy/xalwart.crypto)
  Implements hashing and [JWT](https://jwt.io/) based on the [OpenSSL](https://www.openssl.org/)
  library.

* ### [xalwart.orm](https://github.com/YuriyLisovskiy/xalwart.orm)
  Provides access to relational databases using C++ classes.

* ### [xalwart.server](https://github.com/YuriyLisovskiy/xalwart.server)
  Parses HTTP request headers, creates body readers and sends responses to the client
  represented by [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) socket; this
  is an optional library, any other server can be used which implements the required interface.

* ### [xalwart](https://github.com/YuriyLisovskiy/xalwart)
  Provides all application functional components, such as modules, commands, middleware,
  and controllers.

## Tools
To create a project and its components fast, there is a useful tool called
[Xalwart CLI](https://github.com/YuriyLisovskiy/xalwart-cli), this
[wiki](https://github.com/YuriyLisovskiy/xalwart-cli/wiki) should be helpful.

## Examples
Currently, there is only one very simple example of using the Xalwart web framework.
It is called [OAuth Service](https://github.com/YuriyLisovskiy/oauth-service). More
examples will appear soon in a separate repository. Link to these examples will be
added here.

## License
Xalwart web framework as well as this project is licensed under the
[Apache 2.0 License](LICENSE).
