from tempfile import mkstemp
from shutil import move
from os import remove, close

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

replace('<file_path>',"agentAddress  udp:127.0.0.1:161", "#agentAddress  udp:127.0.0.1:161")
replace('<file_path>',"#agentAddress udp:161,udp6:[::1]:161", "agentAddress udp:161,udp6:[::1]:161")
replace('<file_path>',"#rocommunity public  localhost", "rocommunity public  localhost")
replace('<file_path>',"rocommunity public  default    -V systemonly", "#rocommunity public  default    -V systemonly")
replace('<file_path>',"#  ACCESS CONTROL", "#  ACCESS CONTROL\n#\n #         sec.name  source        community\n com2sec   public    default       public\n com2sec   mynet     10.10.10.0/24 private\n com2sec6  mynet     fec0::/64     private\n #                  sec.model  sec.name\n #group  worldGroup  v1         public\n #group  worldGroup  v2c        public\n group  myGroup     v1         public\n group  myGroup     v2c        public\n #              incl/excl   subtree     [mask]\n view   all     included    .1\n view   sysView included    system\n #              context model level   prefix  read    write  notify (unused)\n access  worldGroup  ""  any  noauth  exact   system  none   none\n access  myGroup     ""  any  noauth  exact   all     all    none\n")
