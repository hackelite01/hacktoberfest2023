#include <iostream>
using namespace std;
int dictionaryContains(string word)
{
    string dictionary[] = {"hello","upesacm","chapter","flash","man","world","forward","and","go","to","acmw","welcome","acm"};
    int size = sizeof(dictionary)/sizeof(dictionary[0]);
    for (int i = 0; i < size; i++)
        if (dictionary[i].compare(word) == 0)
           return true;
    return false;
}
bool wordBreak(string str)
{
    int size = str.size();
 
       if (size == 0)  return true;
    for (int i=1; i<=size; i++)
    {
                if (dictionaryContains( str.substr(0, i) ) &&
            wordBreak( str.substr(i, size-i) ))
            return true;
    }
 
    return false;
}
int main()
{
    string fullName;
    getline (cin, fullName);
    wordBreak(fullName)? cout <<"yes\n": cout << "no\n";
    return 0;
}
