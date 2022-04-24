package com.example.Angularjs.demo;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.Date;
import java.util.Properties;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Multipart;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.MailAuthenticationException;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;


@Service
public class Sendmail implements Isendmail {
	
	
  private JavaMailSender javamail;
  
  @Autowired
  public  ISendmailDAO send;
  
	public void MailService(JavaMailSender javamail) {
		this.javamail = javamail;
	}

	
	
	public String sendmail() 
	{
		String response;
		try
		{
		   Properties props = new Properties();
		   props.put("spring.mail.properties.mail.transport.protocol", "smtp");
		   props.put("spring.mail.properties.mail.smtp.auth", "true");
		   //props.put("spring.mail.properties.mail.smtp.starttls.enable", smtpTLS == 1 ? true : false);
		   props.put("mail.smtp.host", "smtp.gmail.com");
		   props.put("mail.smtp.port", "25");
		  props.put("mail.smp.username", "sdprasadtpg@gmail.com");
		   props.put("mail.smp.password", "Prasad@1998");
		   
		   SimpleMailMessage mail = new SimpleMailMessage();
		  String toaddress = "sdprasadtpg@gmail.com";
		 String Fromaddress ="sdprasadtpg@gmail.com";
		  Session session = Session.getDefaultInstance(props);
		  MimeMessage msg = new MimeMessage(session);
		  Multipart mp = new MimeMultipart();
		  msg.setFrom(new InternetAddress(Fromaddress));
		  msg.setRecipient(Message.RecipientType.TO, new InternetAddress(toaddress));
		  msg.setSubject("Welcome to DXC company");
		  msg.setText("Have a nice day");
		  
		  Transport.send(msg);
		  
		  return "mail send successfully";
		}
		catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	
		return "mail send failed";  
	}
	public String Insert() 
	{
		return send.Insert();
		
	}
	
	

}
