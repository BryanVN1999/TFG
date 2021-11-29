package com.example.heartapp;

import android.app.Activity;
import android.bluetooth.BluetoothGatt;
import android.bluetooth.BluetoothManager;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothAdapter;
import com.google.android.material.snackbar.Snackbar;

import java.util.List;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button continueButton = findViewById(R.id.continueButton);
        continueButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //if(IsArduinoDevice((BluetoothManager)getSystemService(BLUETOOTH_SERVICE)))
                //{
                    Intent toUserData = new Intent(v.getContext(), UserActivity.class);
                    startActivity(toUserData);
                //} else {
                //    Snackbar mySnackbar = Snackbar.make(v, "No estás conectado al Arduino", Snackbar.LENGTH_SHORT);
                //    mySnackbar.show();
                //}
            }
        });
    }
    private boolean IsArduinoDevice(BluetoothManager myManager)
    {
        List<BluetoothDevice> connectedDevices = myManager.getConnectedDevices(BluetoothGatt.GATT);
        if (connectedDevices.size() > 0) {
            // There are paired devices. Get the name and address of each paired device.
            for (BluetoothDevice device : connectedDevices) {
                String deviceName = device.getName();
                String deviceHardwareAddress = device.getAddress(); // MAC address
                if(deviceName.equals("Arduino-BT"))
                {
                    return true;
                }
            }
        }
        return false;
    }
}
