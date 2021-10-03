using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LocalApplicationNET
{
    class Message
    {
        public Guid Id { get; set; }
        public string Platform { get; set; }
        public string Application { get; set; }
        public List<float> Parameters { get; set; }
    }
}
