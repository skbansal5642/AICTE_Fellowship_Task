#
# Add a new langauge by creating a build rule like either cpp or javascript
#
# Checklist:
# - [ ] Add a todo.[java|rb|py] file depending on the language
# - [ ] Copy shared files
# 	1. `README.md`: for the todo-txt-cli problem
# 	2. `todo.test.js`: end-to-end testing using Jest JavaScript framework
# 	3. `package.json`: for installing jest
# 	4. `todo.sh`: template for adding language specific binary
# - [ ] Append language specific executable command to `todo.sh`
#

TARGETS = c cpp javascript ruby java python


all: clean $(TARGETS)
	echo "Packaging completed."

c: _build
	cp -rf c _build
	cp -arf shared/. _build/c
	# Append C compiled binary to `todo.sh`
	# The $@ will pass through CLI args to the binary
	echo \\n./todo.out \"$$\@\" >> _build/c/todo.sh
	echo '\n.\\todo.out %1 %2' >> _build/c/todo.bat
	cat _build/c/Intro.md _build/c/getting_started.md _build/c/Test.md > _build/c/README.md
	rm _build/c/Intro.md _build/c/getting_started.md _build/c/Test.md
	cd _build && zip -r --quiet fellowship-c.zip c -x "node_modules" -x "package-lock.json"
	rm -rf _build/c
	echo "Created C package: fellowship-c.zip"

cpp: _build
	cp -rf cpp _build
	cp -arf shared/. _build/cpp
	# Append C++ compiled binary to `todo.sh`
	# The $@ will pass through CLI args to the binary
	echo \\n./todo.out \"$$\@\" >> _build/cpp/todo.sh
	echo '\n.\\todo.out %1 %2' >> _build/cpp/todo.bat
	cat _build/cpp/Intro.md _build/cpp/getting_started.md _build/cpp/Test.md > _build/cpp/README.md
	rm _build/cpp/Intro.md _build/cpp/getting_started.md _build/cpp/Test.md
	cd _build && zip -r --quiet fellowship-cpp.zip cpp -x "node_modules" -x "package-lock.json"
	rm -rf _build/cpp
	echo "Created C++ package: fellowship-cpp.zip"

javascript: _build
	cp -rf javascript _build
	cp -arf shared/. _build/javascript
	# Append node command to `todo.sh`
	# The $@ will pass through CLI args to the node executable
	echo \\nnode todo.js \"$$\@\" >> _build/javascript/todo.sh
	echo \\nnode todo.js %1 %2 >> _build/javascript/todo.bat
	cat _build/javascript/Intro.md _build/javascript/getting_started.md _build/javascript/Test.md > _build/javascript/README.md
	rm _build/javascript/Intro.md _build/javascript/getting_started.md _build/javascript/Test.md
	cd _build && zip -r --quiet fellowship-javascript.zip javascript -x "node_modules" -x "package-lock.json"
	rm -rf _build/javascript
	echo "Created JavaScript package: fellowship-javascript.zip"

ruby: _build
	cp -rf ruby _build
	cp -arf shared/. _build/ruby
	# Append ruby command to `todo.sh`
	# The $@ will pass through CLI args to the node executable
	echo \\nruby todo.rb \"$$\@\" >> _build/ruby/todo.sh
	echo \\nruby todo.rb %1 %2 >> _build/ruby/todo.bat
	cat _build/ruby/Intro.md _build/ruby/getting_started.md _build/ruby/Test.md > _build/ruby/README.md
	rm _build/ruby/Intro.md _build/ruby/getting_started.md _build/ruby/Test.md
	cd _build && zip -r --quiet fellowship-ruby.zip ruby -x "node_modules" -x "package-lock.json"
	rm -rf _build/ruby
	echo "Created ruby package: fellowship-ruby.zip"

python: _build
	cp -rf python _build
	cp -arf shared/. _build/python
	# Append python command to `todo.sh`
	# The $@ will pass through CLI args to the node executable
	echo \\npython3 todo.py \"$$\@\" >> _build/python/todo.sh
	echo \\npython3 todo.py %1 %2 >> _build/python/todo.bat
	cat _build/python/Intro.md _build/python/getting_started.md _build/python/Test.md > _build/python/README.md
	rm _build/python/Intro.md _build/python/getting_started.md _build/python/Test.md
	cd _build && zip -r --quiet fellowship-python.zip python -x "node_modules" -x "package-lock.json"
	rm -rf _build/python
	echo "Created python package: fellowship-python.zip"

java: _build
	cp -rf java _build
	cp -arf shared/. _build/java
	# Append C++ compiled binary to `todo.sh`
	# The $@ will pass through CLI args to the binary
	echo \\njava Todo \"$$\@\" >> _build/java/todo.sh
	echo \\njava Todo %1 %2 >> _build/java/todo.bat
	cat _build/java/Intro.md _build/java/getting_started.md _build/java/Test.md > _build/java/README.md
	rm _build/java/Intro.md _build/java/getting_started.md _build/java/Test.md
	cd _build && zip -r --quiet fellowship-java.zip java -x "node_modules" -x "package-lock.json"
	rm -rf _build/java
	echo "Created Java package: fellowship-java.zip"

_build:
	mkdir -p _build

clean:
	rm -rf _build
	echo "Removed previous artefacts from _build/ directory."
