#
#  Note: You must run ./setcookie before running make.
#

CC := gcc
CFLAGS := -m32 -static -U_FORTIFY_SOURCE -DCOOKIE=$(shell cat cookie)
LDFLAGS :=
LDLIBS :=

programs := 4.1.1 4.1.2 4.1.3 4.1.4 4.1.5 4.2.1 4.2.2 4.2.3 4.2.4 4.2.5 4.2.6 4.2.7 4.2.8 4.2.9 4.2.10 4.2.11

.PHONY: default clean install uninstall

default: $(programs) permissions

4.1.1: CFLAGS += -w
4.1.2: CFLAGS +=
4.1.3: CFLAGS +=
4.1.4: CFLAGS +=
4.1.5: CFLAGS +=
4.2.1: CFLAGS += -fno-stack-protector -z execstack
4.2.2: CFLAGS += -fno-stack-protector -z execstack
4.2.3: CFLAGS += -fno-stack-protector -z execstack 
4.2.4: CFLAGS += -fno-stack-protector -z execstack 
4.2.5: CFLAGS += -fno-stack-protector -z execstack
4.2.6: CFLAGS += -fno-stack-protector
4.2.7: CFLAGS += -fno-stack-protector -z execstack
4.2.8: CFLAGS += -fno-stack-protector -z execstack
4.2.9: CFLAGS += -fno-stack-protector
4.2.10: CFLAGS += -fno-stack-protector -z execstack
4.2.11: CFLAGS += -fno-stack-protector -z execstack -w

4.1.1: 4.1.1.c helper.c 4.1.1.S
4.1.2: 4.1.2.c helper.c 4.1.2.S
4.1.3: 4.1.3.c helper.c 4.1.3.S
4.1.4: 4.1.4.c helper.c 4.1.4.S
4.1.5: helper.c 4.1.5.S
4.2.1: 4.2.1.c helper.c
4.2.2: 4.2.2.c helper.c
4.2.3: 4.2.3.c helper.c
4.2.4: 4.2.4.c helper.c
4.2.5: 4.2.5.c helper.c
4.2.6: 4.2.6.c helper.c
4.2.7: 4.2.7.c helper.c
4.2.8: 4.2.8.c helper.c
4.2.9: 4.2.9.c helper.c
4.2.10: 4.2.10.c helper.c
4.2.11: 4.2.11.c helper.c

clean:
	rm -f $(programs)

permissions:
	sudo chown root:ubuntu 4.2.[123456789] 4.2.10 4.2.11 4.1.5
	sudo chmod 6777 4.2.[123456789] 4.2.10 4.2.11 4.1.5
	
