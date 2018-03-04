using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DataPlotter : MonoBehaviour {

    public string inputfile;

    private List<Dictionary<string, object>> pointList;

    public int columnx = 0;
    public int columny = 1;

    public string xName;
    public string yName;

    public GameObject PointPrefab;

	// Use this for initialization
	void Start () {
        pointList = CSVReader.Read(inputfile);
        Debug.Log(pointList);
        List<string> columnList = new List<string>(pointList[1].Keys);
        Debug.Log("There are " + columnList.Count + " columns in CSV");
        foreach (string key in columnList)
            Debug.Log("Column name is " + key);
        xName = columnList[columnx];
        yName = columnList[columny];
        for (var i=0; i < pointList.Count; i++)
        {
            float x = System.Convert.ToSingle(pointList[i][xName]);
            float y = System.Convert.ToSingle(pointList[i][yName]);
            Instantiate(PointPrefab, new Vector2(x, y), Quaternion.identity);
        }


	}
	

}
