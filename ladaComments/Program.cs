using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Speech;
using System.Net;
using HtmlAgilityPack;

namespace ladaComments
{
    class Program
    {
        static void Main(string[] args)
        {
            WebClient webClient = new WebClient();

            HtmlDocument htmlDoc = new HtmlDocument();
            htmlDoc.OptionFixNestedTags = true;

            List<string> articles = new List<string>();
            List<string> lastArticles = new List<string>();


            for (;;)
            {
                string res = webClient.DownloadString("https://www.lada.kz/index.php?do=lastcomments").Replace("--!>","-->");
                htmlDoc.LoadHtml(res);
                foreach (HtmlNode node in htmlDoc.DocumentNode.SelectNodes("//div[@class='comment-text']/div"))
                    articles.Add(node.InnerText);
                int top = 0;
                if (lastArticles.Count > 0)
                    while (articles[top] != lastArticles[0])
                        top++;
                else
                    top = articles.Count;
                for (int i = top - 1; i >= 0; i--)
                {
                    Console.WriteLine(articles[i] + "\n\n");
                }
                lastArticles = articles;
            }
        }
    }
}
