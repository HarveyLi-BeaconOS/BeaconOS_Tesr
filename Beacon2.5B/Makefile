
exec: MShell4.py
	pyinstaller MShell4.py \
	--onefile \
	--collect-all gnureadline \
	--collect-all maskpass \
	--name BeaconExecutable \
	--distpath ~/Desktop/BeaconOS/src/Beacon2.4

base: MShell4.py
	pyinstaller MShell4.py \
	--onefile \
	--collect-all gnureadline \
	--collect-all maskpass \

clean:
	rm -rf dist build MShell4.spec MShell4 BeaconExecutable BeaconExecutable.spec
 