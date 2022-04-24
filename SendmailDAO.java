package com.example.Angularjs.demo;

import java.io.FileInputStream;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

import org.springframework.boot.autoconfigure.jdbc.JdbcTemplateAutoConfiguration;
import org.springframework.stereotype.Repository;

@Repository
public class SendmailDAO implements ISendmailDAO {
	
   
	
	public String Insert()
	{
		try {
			
			Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "Hr", "root");
			
			PreparedStatement ps = conn.prepareStatement("Insert into country values(?,?,?)");
			ps.setString(1, "India");
			InputStream in = new FileInputStream("C:\\Users\\dsakhinetipa\\Downloads\\india.jpg");
			ps.setBlob(2, in);
		    ps.setString(3, "JAI HINDH");
		    ps.execute();
		    return "record inserted";
		
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	    return "record not inserted";
		
	}

}
