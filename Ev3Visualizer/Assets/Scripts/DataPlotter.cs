using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEditor;


public class DataPlotter : MonoBehaviour
{

    public string inputfile;

    private List<Dictionary<string, object>> pointList;

    public int columnx = 0;
    public int columny = 1;

    public string xName;
    public string yName;

    public GameObject PointPrefab;


    // Use this for initialization
    [MenuItem("Select .csv")]
    void Start()
    {
        //Texture2D texture = Selection.activeObject as Texture2D;
        //if (texture == null)
        //{
        //    EditorUtility.DisplayDialog("Select Texture", "You must select a texture first!", "OK");
        //    return;
        //}
        pointList = CSVReader.Read(inputfile);
        Debug.Log(pointList);
        List<string> columnList = new List<string>(pointList[1].Keys);
        Debug.Log("There are " + columnList.Count + " columns in CSV");
        foreach (string key in columnList)
            Debug.Log("Column name is " + key);
        xName = columnList[columnx];
        yName = columnList[columny];
        for (var i = 0; i < pointList.Count; i++)
        {
            float x = System.Convert.ToSingle(pointList[i][xName]);
            float y = System.Convert.ToSingle(pointList[i][yName]);
            Instantiate(PointPrefab, new Vector2(x, y), Quaternion.identity);
        }
    }
}
