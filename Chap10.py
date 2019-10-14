import time_series


class chap10:
    def  skip_header(self, reader):
        line = reader.readline()
        line = reader.readline()
        while line.startswith('#'):
            line = reader.readline()

        return line
    def practice1(self):
        name = input("What is the name of the file?")
        bk_name = name + '.bak'
        backup = open(bk_name, 'w')
        for line in open(name): backup.write(line)
        backup.close()

    def practice2(self):
        alkaline_metals = []
        for line in open('alkaline_metals.txt'):
            alkaline_metals.append(line.strip().split(' '))

    def practice4(self, reader):
        line =  skip_header(reader).strip()
        print(line)
        print(reader.read())

    def practice5(self, reader):
        line = time_series.skip_header(reader).strip()
        smallest = int(line)
        for line in reader:
            line = line.strip()
            if line != '-':
                value = int(line)
                smallest = min(smallest, value)

        return smallest

        if __name__ == '__main__':
            with open('hebron.txt', 'r') as input_file:
                print(smallest_value_skip(input_file))

    def practice6(self, reader):
        line = time_series.skip_header(reader).strip()
        smallest = int(line)
        for line in reader:
            line = line.strip()
            if line != '-':
                continue

        return smallest

        if __name__ == '__main__':
            with open('hebron.txt', 'r') as input_file:
                print(smallest_value_skip(input_file))

    def practice7(self, reader):
        line = reader.readline()
        if not line:
            return None
        if not (line.startswith('CMNT') or line.isspace()):
            key, name = line.split()
            molecule = [name]
        else:
            molecule = None
        reading = True
        while reading:
            line = reader.readline()
            if line.startswith('END'):
                reading = False
            elif not (line.startswith('CMNT') or line.isspace()):
                key, num, atom_type, x, y, z = line.split()
                if molecule == None:
                    molecule = []
                    molecule.append([atom_type, x, y, z])

        return molecule

    def practice8(self, reader):
        line = reader.readline()
        if not line:
            return None
        key, name = line.split()
        molecule = [name]
        reading = True
        serial_number = 1
        while reading:
            line = reader.readline()
            if line.startswith('END'):
                reading = False
            else:
                key, num, atom_type, x, y, z = line.split()
                if int(num) != serial_number:
                    print('Expected serial number {0}, but got {1}'.format(serial_number, num))
                    molecule.append([atom_type, x, y, z])
                    serial_number += 1

        return molecule