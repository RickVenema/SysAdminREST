pdoc --html -o docs . --force

mkdir docs\API\
mkdir docs\Tests\

for %%F in (docs\SysAdminREST\*) do move /Y %%F docs\
for %%F in (docs\SysAdminREST\API\*) do move /Y %%F docs\API\
for %%F in (docs\SysAdminREST\Tests\*) do move /Y %%F docs\Tests\

rmdir docs\SysAdminREST\API
rmdir docs\SysAdminREST\Tests
rmdir docs\SysAdminREST\