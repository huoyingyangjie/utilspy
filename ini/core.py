# Author yangjiegogogo@gmail.com


class INI(object):
    class Section(object):
        def __init__(self, name):
            self.name = name
            self.kv ={}

    def __init__(self, file_path):
        self.global_section = None
        self.local_sections = []
        self.__parse__(file_path)

    def __read__(self, file_path):
        with open(file_path) as f:
            text = f.read()
        return text

    def __parse__(self, file_path):
        text = self.__read__(file_path)
        text_lines = text.split("\n")
        text_lines_strip = []
        for i in text_lines:
            i = i.strip()
            if i == "":
                continue
            if len(i) > 0 and i[0] == '#':
                continue
            text_lines_strip.append(i)
        section = None
        for line in text_lines_strip:
            if len(line) < 2:
                raise Exception("too few characters")
            if line[0] == '\\' and line[1] == '\\':
                continue
            if line[0] == '[' and line[len(line)-1] == ']':
                line_list = list(line)
                line_list[0] = ""
                line_list[len(line_list)-1] = " "
                line = ''.join(line_list)
                line = line.strip()
                name = line
                section = self.Section(name)
                self.local_sections.append(section)
                continue
            if line[0] == '=':
                raise Exception("illegal beginning of line")
            if '=' not in line:
                raise Exception("no split character")
            if section is None:
                section = self.Section(None)
                self.global_section = section
            index = line.find('=')
            key = line[0:index]
            key = key.strip()
            value = line[(index+1):len(line)]
            value = value.strip()
            if key in section.kv:
                raise Exception("redundant key")
            section.kv[key] = value

    def section_count(self, name):
        count = 0
        for section in self.local_sections:
            if section.name == name:
                count += 1
        return count

    def find(self, index, name, key):
        cursor = 0
        section = None
        if name is None:
            section = self.global_section
        else:
            for local_section in self.local_sections:
                if local_section.name != name:
                    continue
                if cursor != index:
                    cursor += 1
                    continue
                section = local_section
                break
        if section is None:
            return None
        if key in section.kv:
            return section.kv[key]
        else:
            return None
